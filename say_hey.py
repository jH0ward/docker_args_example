import sys

# Not needed after adding the CMD to Docker

#if len(sys.argv) > 1:
#    addressee = sys.argv[1]
#else:
#    addressee = 'partner'



print(f'Got {len(sys.argv)} args')
for a in sys.argv:
    print(a)

addressee = sys.argv[1]

print(f'\n Well hey there {addressee}!')
