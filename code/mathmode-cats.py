# mathmode-cats.py
# Generate a cute little cat face for LaTeX
# Requires amsmath, amssymb, graphics, wasysym

import random as r

wink_eyes = ['\\circ', '\\circledast', '\\circledcirc', '\diamond',
             '\\mathbb{O}', '\\mathfrak{O}', '\\odot', '\\sigma']
no_wink_eyes = ['-', '=', '\\bigstar', '\\blacksquare', '\\cup', '\\equiv',
                '\\newmoon', '\\square']
eye_pairs = [('\\eqslantgtr', '\\eqslantless'),
             ('\\mathfrak{O}', '\\reflectbox{$\\mathfrak{O}$}')]
mouths = ['\\ ', '_\\bot', '_\\curlywedge', '_\\diamond', '_\\downarrow',
          '_\\heartsuit', '_\\mathfrak{I}', '_\\mathfrak{J}', '_\\nu',
          '_\\omega', '_\\tau', '_\\trianglelefteq', '_\\trianglerighteq', '_r',
          '_w', '_x']
cheek_list = [('(', ')'), ('_( \\ ', '\\ _)')]

wink_right = list((eye, '-') for eye in wink_eyes)
wink_left =  list(('-', eye) for eye in wink_eyes)
no_winks = list(zip(no_wink_eyes, no_wink_eyes))

all_eyes = wink_left + wink_right + no_winks + eye_pairs

# Single cat face
(mouth, cheeks, eyes) = (r.choice(mouths), r.choice(cheek_list),
                         r.choice(all_eyes))
str = ('$\hat{' + cheeks[0] + eyes[0] + '} ' + mouth
      + ' \hat{' + eyes[1] + cheeks[1] + '}$')
print('A cat just wandered in!')
print(str)

# All cat faces
#face_list = [(mouth, cheeks, eyes) for mouth in mouths
#             for cheeks in cheek_list for eyes in all_eyes]
#for (mouth, cheeks, eyes) in r.sample(face_list, len(face_list)):
#    str = ('$$\hat{' + cheeks[0] + eyes[0] + '} ' + mouth + ' \hat{' + eyes[1]
#          + cheeks[1] + '}$$')
#    print(str)
