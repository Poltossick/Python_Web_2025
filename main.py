# Библиотека pymorphy
import pymorphy3

# morph = pymorphy3.MorphAnalyzer() # -> морфологический анализ слова
#
# print(morph.parse('Дмитрий'))
# """
# [Parse(word='дмитрий', tag=OpencorporaTag('NOUN,anim,masc,Name sing,nomn'),
# normal_form='дмитрий', score=0.985915, methods_stack=((DictionaryAnalyzer(),
# 'дмитрий', 61, 0),)), Parse(word='дмитрий', tag=OpencorporaTag('NOUN,anim,femn,Name plur,gent'),
# normal_form='дмитрия', score=0.007042, methods_stack=((DictionaryAnalyzer(), 'дмитрий', 64, 8),)),
# Parse(word='дмитрий', tag=OpencorporaTag('NOUN,anim,femn,Name plur,accs'), normal_form='дмитрия',
# score=0.007042, methods_stack=((DictionaryAnalyzer(), 'дмитрий', 64, 10),))]
# """

from pymorphy3 import MorphAnalyzer

form = MorphAnalyzer().parse('бутылка')[0]
for btl in reversed(range(99)):
    print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl + 1).word} пива.')
    print('Возьмем одну и выпьем')
    if btl % 10 == 1 and btl != 11:
        remain = 'Осталась '
    else:
        remain = 'Осталось '
    print(f'{remain}{btl} {form.make_agree_with_number(btl).word} пива.')
