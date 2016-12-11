'''
Author: Nicholas Gilpin
Description:
    Succeed is a program which aims to formulate the optimal routine for a
    person to succeed in life.
'''
# Universal Variables
dead = False
successful = False


class Need:
    """ Needs: true if satified and false if not satisfied"""
    # importance_levels:
    # 0'accomplishment'
    # 1'esteem'
    # 2'love'
    # 3'saftey'
    # 4'biological'

    def __init__(self, satisfied, importance_level, name):
        self.satisfied = satisfied
        self.importance_level = importance_level
        self.name = name

    def __lt__(self, other):
        return self.importance_level < other.importance_level


def list_needs():
    """ Create a list of common needs """
    hierarchy = [
        ['accomplishment'],
        ['selfRespect', 'communityRespect'],
        ['friendship', 'family', 'intimacy'],
        ['physical', 'financial', 'health'],
        ['air', 'food', 'water', 'shelter', 'warmth', 'sleep', 'sex']
    ]
    needs = []
    for i, group in enumerate(hierarchy):
        for need in group:
            needs.append(Need(False, i + 1, need))
    return needs


def check(need):
    need_state = input("Are your " + str(need) + " needs taken care of (y/n)?")
    result = False
    if (need_state == 'y'):
        result = True
    return result

# Auxillary routines


def satify(need):
    return True


def list_goals(priorities):
    print("\n importance goal")
    print("-------------------------------")
    for goal in sorted(priorities, reverse=True):
        print(str(goal.importance_level) + " " + str(goal.name))
# Main routine


def succeed():
    """ To survive and thrive, keep calling this function until death """
    needs = list_needs()
    priorities = []
    for need in needs:
        need.satisfied = check(need.name)
        if (need is True):
            continue  # Nothing needs to be done
        else:
            if (need.importance_level > 3):
                if (need.name != "sex"):
                    print("Handle your " + str(need.name) + " need now!")
                    print("Don't return until finished!")
                priorities.append(need)
                need = satify(need)
            else:
                # Mark a non-critical need for solving later
                priorities.append(need)
    list_goals(priorities)

succeed()
