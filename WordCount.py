#WordCount.py
#Name: Mason Rodgers
#Date: 3/2/25
#Assignment: word count

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    letterCount = letterCount + len(line)
  
    
  print("Lines:", lineCount)  
  print("Words:", wordCount)
  print("Characters:", letterCount)

if __name__ == '__main__':
  main()
