# task is to docker-cleaup automation
'''
first check the exited containers
then print those names
then remove that containers
then remove that used images
'''
import subprocess

def get_containers():
    result= subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}} {{.Status}}"], stdout=subprocess.PIPE, text=True)

    exited = []


    for lines in result.stdout.splitlines():
        name, status = lines.split(" ", 1)

        if "Exited" in lines:
        
            exited.append(name)
    return exited

def remove_containers(container):
    for c in container:
        print(f"removing the containers {c}")
        result = subprocess.run(["docker", "rm", c], stdout=subprocess.PIPE, text=True)

def images():
    print("removing docker images..")
    result=subprocess.run(["docker", "image", "prune", "-a", "-f"])

def main():
    exited = get_containers()

    if not exited:
        print("There is no exited containers")

    else:
        remove_containers(exited)

    images()

main()









