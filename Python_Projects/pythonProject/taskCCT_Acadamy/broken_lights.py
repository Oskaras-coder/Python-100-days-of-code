import itertools

DISTANCE_BETWEEN_STREET_LIGHTS = 20                                                               # CONSTANTS AND INPUT VALUES
ROAD_LENGTH = 200
NOT_WORKING_STREET_LIGHTS = [4, 5, 6]


def intensity_calculator(first_light, second_light):                                              # Calculates light's intensity
    index_distance = abs(first_light - second_light)
    relative_intensity = 3 ** (-pow((DISTANCE_BETWEEN_STREET_LIGHTS * index_distance / 90), 2))
    return relative_intensity


def find_index_of_darkest_street_light(road_length, not_working_street_lights, **karma):
    lights_number = int(road_length / DISTANCE_BETWEEN_STREET_LIGHTS + 1)                         # total amount of lights
    index_intensities = {}                                                                        # broken lights' index and their illumination intensities will be kept in a dictionary

    for lights in not_working_street_lights:                                                      # every broken light is stored in a dictionary
        cumulative_intensity = 0
        for another_light in range(lights_number):                                                # every illumination intensity at the light's position is stored in a dictionary
            if another_light not in not_working_street_lights:
                lights_relative_intensity = intensity_calculator(lights, another_light)
                if lights_relative_intensity > 0.01:                                              # if light's illumination is below 0,01, it's ignored
                    cumulative_intensity += lights_relative_intensity                             # every other working light is adding their illumination to non-working light's position
            index_intensities[lights] = cumulative_intensity
    least_illuminated_index = min(index_intensities, key=index_intensities.get)                   # finding the lowest intensity in a dictionary
    if karma:                                                                                     # returns values for the optional task
        return index_intensities
    else:                                                                                         # returns the answer if karma is not true
        return least_illuminated_index


def find_min_lights():                                                                            # function calculating minimal number of light bulbs
    first_checked_light = 0
    minimum_lights = 0

    while first_checked_light < len(NOT_WORKING_STREET_LIGHTS):
        changeable_light = []

        for index in range(first_checked_light, len(NOT_WORKING_STREET_LIGHTS) + 1):              # to reduce calculation time broken lights' areas are separated into different blocks
            changeable_light.append(NOT_WORKING_STREET_LIGHTS[index])
            first_checked_light = index + 1
            try:
                intensity = intensity_calculator(NOT_WORKING_STREET_LIGHTS[index], NOT_WORKING_STREET_LIGHTS[index + 1])
                if intensity < 0.01:                                                              # if the next block is too far the light's intensities from there are ignored
                    break
            except:
                break
        first_checked_light = first_checked_light + 1                                             # the next block which is too far will be calculated starting from the first index in that block
        found_min = False
        for minimum_lamps_required in range(len(changeable_light) + 1):
            for combination in itertools.combinations(set(changeable_light), minimum_lamps_required):      # trying all possible combinations from 0 to minimum required changed lights in that area
                new_list = [light for light in changeable_light if light not in combination]
                changed_lights = find_index_of_darkest_street_light(road_length=ROAD_LENGTH,
                                                                    not_working_street_lights=new_list,
                                                                    karma=True)
                if min(changed_lights.values()) >= 1:                                             # if all area is illuminated more than 1 the loop is stopped
                    found_min = True
                    minimum_lights += minimum_lamps_required
                    break
            if found_min:
                break

    return minimum_lights                                                                         # returns the minimal number of light bulbs, which is needed to be replaced


if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=ROAD_LENGTH, not_working_street_lights=NOT_WORKING_STREET_LIGHTS) == 5
    print("ALL TESTS PASSED")

    print(find_index_of_darkest_street_light(road_length=ROAD_LENGTH,
                                             not_working_street_lights=NOT_WORKING_STREET_LIGHTS))  # For evaluation
    print(find_min_lights())                                                                        # For karma points