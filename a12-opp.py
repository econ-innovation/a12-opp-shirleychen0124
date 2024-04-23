# Define a class to manage paper attributes and interactions
class Paper:
    def __init__(self, ut, year, journal, issn, doi, issue, volume):
        self.ut = ut
        self.year = year
        self.journal = journal
        self.issn = issn
        self.doi = doi
        self.issue = issue
        self.volume = volume
    
    def append_to_file(self, filename):
        # Append paper details to a file
        with open(filename, 'a') as file:
            file.write(f"UT: {self.ut}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Journal: {self.journal}\n")
            file.write(f"ISSN: {self.issn}\n")
            file.write(f"DOI: {self.doi}\n")
            file.write(f"Issue: {self.issue}\n")
            file.write(f"Volume: {self.volume}\n\n")

    @classmethod
    def from_text(cls, text):
        # Create an instance from a text line
        details = text.strip().split(': ')[1]
        attributes = [line.strip().split(': ')[1] for line in details.split('\n')]
        return cls(*attributes)

# Utility function to extract the next value from a line of text
def extract_next_value(current_line):
    return current_line.split(':')[1].strip()

# Load papers from a file and create Paper objects
papers = []
with open('qje2014_2023.txt', 'r') as file:
    content = file.readlines()
    index = 0
    while index < len(content):
        details = [extract_next_value(content[index + offset]) for offset in range(7)]
        papers.append(Paper(*details))
        index += 7

# Save all papers to an output file
for paper in papers:
    paper.append_to_file('output.txt')

# Read from output file and display each paper's details
with open('output.txt', 'r') as file:
    for line in file:
        if line.strip():
            paper = Paper.from_text(line)
            print(f"UT: {paper.ut}")
            print(f"Year: {paper.year}")
            print(f"Journal: {paper.journal}")
            print(f"ISSN: {paper.issn}")
            print(f"DOI: {paper.doi}")
            print(f"Issue: {paper.issue}")
            print(f"Volume: {paper.volume}\n")
