import pandas as pd

df = pd.read_excel('database.xlsx')





me = 'M.S.BS'
copyright = "This programme created by: " + 'Mohammed Saleh Bin Suwad'
discribtion = 'الوصف:-\nيعمل هذا البرنامج على البحث عن الاسم المُدخل ثم يخرج معلومات مرتبة عن الرغبات مثل الترتيب ونسبة  الطالب/ة في الثنوية العامة ونسبته/ها في امتحان القبول..الخ '
note = '\n\nملاحظة:-\nيعمل هذا البرنامج على متنافسي السنة الدراسية(٢٠٢٢ - ٢٠٢١) في جامعة حضرموت فقط.'
dan = "\n\nتنبيـــــه:-\nيمنع انساب البرنامج لغير صاحبه. يمكن استخدامه للاغراض التعليمية"
contact = '\n\nللتواصل والاستفسار:-\nجوال: ٧١١٤٩١٧٩٧\nجيميل: mbinsuwad@gmail.com'

a = '\t ####\t\t\t\t####'
b = '\t  ###\t\t\t\t ###'
c = '\t \t \t ]|['
d = '\t \t \t [^]'
e = '\t \t\t(|π|)'
f = '\t \t °=.π#[=]#{÷}#[=]#π.=°`'
g = '\t\t.\t\t\t.'
h = '\t \t .;=#[=]×{÷}×[=]#=:.\n\n'
i = '\t\t\t_.<=>._'
j = '\t\t\t°<=>°\n\n'
s = ' '


def smile():
    print(s)
    print(s)
    print(a)
    print(a)
    print(b)
    print(s)
    print(c)
    print(d)
    print(d)
    print(e)
    print(s)
    print(s)
    print(g)
    print(f)
    print(j)


def sad():
    print(s)
    print(s)
    print(a)
    print(a)
    print(b)
    print(s)
    print(c)
    print(d)
    print(d)
    print(e)
    print(s)
    print(s)
    print(i)
    print(h)


smile()
print('مرحبــاً بــك\n\n\n')
print(copyright + '\n')
print(contact + '\n')
print(discribtion)
print(note + '\n')
print(dan + '\n')
# print()
while True:
    name = input('Enter name in arbic: ')
    div = name.split(' ')
    length = len(div)

    if length == 1:
        for a in range(len(df['name'])):
            if div[0] in str(df.loc[a]['name']).split(' '):
                if df.loc[a]['sex'] == 'أنثى':
                    print('حصلت الطالبة: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')
                else:
                    print('حصل الطالب: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')

    if length == 2:
        for a in range(len(df['name'])):
            l = str(df.loc[a]['name']).split(' ')
            if (div[0] in l) and (div[1] in l):
                if df.loc[a]['sex'] == 'أنثى':
                    print('حصلت الطالبة: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')
                else:
                    print('حصل الطالب: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')

    if length == 3:
        for a in range(len(df['name'])):
            l = str(df.loc[a]['name']).split(' ')
            if (div[0] in l) and (div[1] in l) and (div[2] in l):
                if df.loc[a]['sex'] == 'أنثى':
                    print('حصلت الطالبة: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')
                else:
                    print('حصل الطالب: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')

    if length == 4:
        for a in range(len(df['name'])):
            l = str(df.loc[a]['name']).split(' ')
            if (div[0] in l) and (div[1] in l) and (div[2] in l) and (div[3] in l):
                if df.loc[a]['sex'] == 'أنثى':
                    print('حصلت الطالبة: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')
                else:
                    print('حصل الطالب: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')

    if length == 5:
        for a in range(len(df['name'])):
            l = str(df.loc[a]['name']).split(' ')
            if (div[0] in l) and (div[1] in l) and (div[2] in l) and (div[3] in l) and (div[4] in l):
                if df.loc[a]['sex'] == 'أنثى':
                    print('حصلت الطالبة: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')
                else:
                    print('حصل الطالب: ' + str(df.loc[a]['name']) + ' في تخصص ' + str(
                        df.loc[a]['specialty']) + ' على الترتيب: ' + str(
                        df.loc[a]['order']) + '\nنسبة الثنوية: ' + str(
                        df.loc[a]['S.school']) + '\nنسبة امتحان القبول: ' + str(
                        df.loc[a]['test']) + '\nالنسبة النهائية : ' + str(
                        df.loc[a]['finall']) + '\n\n\t\t' + me + '\n\n')