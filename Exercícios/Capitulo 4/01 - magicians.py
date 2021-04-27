magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} that was a great trick.")
    print(f"I cant't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone that was a great magic show!")

#intentional indenting error
# for magicina in magicians:
# print(magician)

#intentional indenting showing behaviours of not indented code causing a logical error
# for magician in magicians:
#   print(f"{magician.title()} that was a great trick.")
# print(f"I cant't wait to see your next trick, {magician.title()}.\n")

#intentional unecessary indenting after the loop
# for magician in magicians:
#     print(f"{magician.title()} that was a great trick.")
#     print(f"I cant't wait to see your next trick, {magician.title()}.\n")
#     print("Thank you everyone that was a great magic show!")

#forcing error removin colon from the for loop
# for magician in magicians
#     print(magician)