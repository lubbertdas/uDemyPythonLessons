import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0
tries = 3

print("we hate you, please die")
inpat = input("press enter to continue")
print("get ready in...")

for i in reversed (range (3)):
    print (i+1)
    t.sleep(0.5)


mistakes = 0
while len(times) < tries:
    start = t.time()
    word = input("type the Spaß: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word != "asdf"):
        mistakes += 1

print("mistakes: ", mistakes)
print(times)

x = [1,2,3]
y = times
plt.plot(x,y)
legend = []
for i in range (tries):
    legend.append(i+1)   
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing eVolutiOn')
plt.show()

