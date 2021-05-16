from enum import Enum

class Countries(Enum):

     Afghanistan = 93

     Albania = 355

     Algeria = 213

     Andorra = 376

     Angola = 244

     Antarctica = 672

print('\nMember name : {}'.format(Countries.Albania.name))

print('Member value : {}'.format(Countries.Albania.value))
