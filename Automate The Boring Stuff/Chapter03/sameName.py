def spam():
    eggs = 'spam local'
    # print spam local
    print(eggs)
    
def bacon():
    eggs = 'bacon local'
    # print bacon local
    print(eggs)
    # print spam local
    spam()
    # print bacon local
    print(eggs)

eggs = 'global'
# execute bacon()
bacon()
#print global
print(eggs)
    