
file = "killsays.txt"
lithium_file = "lithium_killsays.cfg"
    
def replace_foreign_shit(line): # In case of your killsays having foreign variables, you can change them here. Refer to https://lithiumcheats.mybb.us/viewtopic.php?id=2080 for lithium killsay variables. Replacement below is for NCC variables.
   im_stuff = line.rstrip().replace("%victim%", "%player_name%")
   return im_stuff

def main():
    try:
        f = open(file, "r")
        f_lithium = open(lithium_file, "w+")
        killsays = []
        count_of_killsays = 0
        for line in f:
            count_of_killsays += 1
            killsays.append('alias lithium_killsay' + str(count_of_killsays) + ' "say ' + replace_foreign_shit(line) + '"\n')
            f_lithium.write(killsays[count_of_killsays - 1])
        f.close()
        f_lithium.close()
        print("Number of killsays saved: ", count_of_killsays)
    except FileNotFoundError:
        print("You didn't create killsays.txt file.")
    except Exception as e:
        print("Unexpected error: %s" % e)
if __name__== "__main__":
    main()