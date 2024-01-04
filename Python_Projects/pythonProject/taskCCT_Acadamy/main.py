"""
There are street lights placed evenly every 20 meters on a straight road.
Most of the street lights are working and have the same illumination intencity.
Non-working street lights are provided as a list of their indexes.
If a street light is not working - its position can still be illuminated by neighboring lights.
Illumination is decreasing exponentially when the distance increases from a street light.
Please find an index of a street light, which has the lowest illumination. Its light bulb will be replaced.
Notes:
- The road lenght can be from 0 to 2000000m.
- The street lights are indexed from 0 and the first one stands at the begining of the road.
- The intensity of illumination can be calculated using f(x) = 3^(-(x/90)^2) formula,
  where x is a distance from the street ligth in meters.
- If the street light is very far away and its illumination intencity is less than 0.01 - its illumination has to be ignored.
- In case there are several street lights with the same lowest illumination - provide the one with the lowest index.
Example:
road_length = 200
non_working_street_lights = [4, 5, 6]
The length of the road is 200 meters and it has 11 street lights on it. Lights with indexes 4, 5 and 6 are not working.
The bulb of the street light with index 5 has to be replaced, because the illumination at it is the lowest.
Optional (for extra Karma points):
- Please find the minimal number of light bulbs, which is needed to be replaced
  to make cumulative illumination intencity at every street light non less than 1.
"""
DISTANCE_BETWEEN_STREET_LIGHTS = 20


def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    lights_number = int(road_length / DISTANCE_BETWEEN_STREET_LIGHTS + 1)
    index_intensities = {}

    for lights in not_working_street_lights:
        cumulative_intensity = 0
        for another_light in range(lights_number):
            if another_light not in not_working_street_lights:
                index_distance = abs(lights - another_light)
                lights_relative_intensity = 3 ** (-pow((DISTANCE_BETWEEN_STREET_LIGHTS * index_distance / 90),
                                                       2))  # intensity calculation between lights, if x == 0,
                # intensity == 1
                if lights_relative_intensity > 0.01:
                    cumulative_intensity += lights_relative_intensity
        index_intensities[lights] = cumulative_intensity
    least_illuminated_light = min(index_intensities, key=index_intensities.get)

    return least_illuminated_light



if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("ALL TESTS PASSED")
