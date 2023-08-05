"""
Author: Dmitri Lyalikov
Email:  Dlyalikov01@manhattan.edu
Date of last revision: 04/28/2023

Status:
    in development / validating

feature_extract.py
    This module performs characteristic feature extraction on the x and y coordinates of an
    edge profile.
    These methods derive numerical profile characteristics of the pendant drop
        - Apex Radius: Found with circle fit approximation
        - Equator Radius
        - Radius_S: Radius at y = 2 * (Equator Radius
        - Drop_Height
        - Capillary Radius
    By instantiating a FeatureExtract object with the x, y profile coordinates, all of these features
    are automatically saved to a dictionary: self.feature_set as a key, value pair
"""

import numpy as np
from circle_fit import taubinSVD


class FeatureExtract:
    def __init__(self, x: list[int], y: list[int]):
        """
        :param x: globally used ordered set of x coordinates of the pendant drop profile
        :param y: globally used ordered set of x coordinates of the pendant drop profile
        """

        self.x = x
        self.y = y

        self.capillary_radius = self.x[-1]
        self.drop_height = self.y[0]
        self.equator_radius = self.find_equator_radius()
        self.s_radius = self.find_s_radius()
        self.apex_radius = self.find_apex_radius()
        # Normalize to dimensionless ratio to apex radius
        self.feature_set = {
            "Drop height": self.drop_height / self.apex_radius,
            "Capillary radius": self.capillary_radius / self.apex_radius,
            "R-s": self.s_radius / self.apex_radius,
            "R-e": self.equator_radius / self.apex_radius,
        }
        print(f"Apex radius (Pixels): {self.apex_radius }")
        print(f"Equator radius: {self.equator_radius }\n"
              f"S radius: {self.s_radius }\n"
              f"Capillary radius: {self.capillary_radius}\n"
              f"Drop Height: {self.drop_height }")

    def average_x(self, i: int, n: int) -> int:
        s = 0
        for j in range(i-n, i+n+1):
            s = s + self.x[j]
        return s / (2 * n + 1)

    def recursive_equator_radius(self, i, n):
        # use recursive approach: start from apex, continue until x decreases
        # at i-th point we average x of x-n to x+n to suppress noise
        # compare x-i_th vs x_i+t_th until it decreases to find equator
        if self.average_x(i, n) < self.average_x(i+1, n) and i <= len(self.x) - n-3:
            i += 1
            output = self.recursive_equator_radius(i, n)
            if output:
                self.equator_radius = output
        else:
            if i <= len(self.x) * 0.7:
                # assumed 70% of drop is enough for the equator radius
                return self.x[i]
            else:
                return

    def find_re_rs(self, n=5) -> (int, int):
        # Finding Equator Radius (Re) and Rs @ y=2Re
        """
        ;param self:
        :param n:
        :return: tuple (equator_radius: int, s_radius: int)
        """

        i = n
        self.equator_radius = 0
        # A recursive function that returns equator radius
        self.recursive_equator_radius(i, n)
        if self.equator_radius == 0:

            # equator radius is 0: drop is not well-deformed: Beta>0.7
            # find equator radius from circle fitting
            # select 40% of the total number of points for circle fitting
            num_points_to_circlefit = round(0.4 * len(self.x))
            points_rh_circlefit = np.stack(
                (self.x[:num_points_to_circlefit],
                 self.y[:num_points_to_circlefit]), axis=1)
            xc, yc, self.equator_radius, sigma = taubinSVD(points_rh_circlefit)

        # Find s_radius at y = 2 * equator_radius
        if self.equator_radius < 0.5 * self.drop_height:
            # res = index of y if y > 2 * equator_radius
            res = next(xx for xx, val in enumerate(self.y) if val > 2 * self.equator_radius)
            self.s_radius = self.x[res]
        else:
            # Drop is too small
            self.s_radius = self.capillary_radius
        return self.equator_radius, self.s_radius

    # Use Circle fit to approximate apex radius of edge profile
    # ratio_drop_length: 1 >= float value > 0 representing number points along profile to approximate with
    # change_ro: float value representing minimum value of change in circle radius before stopping approximation
    def find_apex_radius(self, ratio_drop_length: float = 0.15, change_ro: float = .005) -> float:

        num_point_ro_circlefit = round(len(self.x) * ratio_drop_length) + 1

        percent_drop_ro = 0.1
        i = 0
        diff = 0
        r0 = 0
        r_0 = []
        while diff >= change_ro*r0 or num_point_ro_circlefit <= percent_drop_ro * len(self.x):
            points_ro_circlefit = np.stack((self.x[:num_point_ro_circlefit], self.y[:num_point_ro_circlefit]), axis=1)
            xc, yc, r0, sigma = taubinSVD(points_ro_circlefit)
            r_0.append(r0)
            if i > 1:
                diff = abs(r_0[i] - r_0[i-1])
            i += 1
            num_point_ro_circlefit += 1

        return r_0[-1]

    # Find maximum (bulge) x value from 70% of profile
    def find_equator_radius(self):
        split = int(len(self.x) * 0.7)

        # Slice the first 70% of the list from bottom and find the maximum value
        return max(self.x[:split])

    # Find radius at point X = [2 * equator_radius] between capillary and equator
    def find_s_radius(self):
        return self.x[-2 * int(self.equator_radius)]
