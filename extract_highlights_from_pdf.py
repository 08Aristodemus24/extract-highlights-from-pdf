import fitz



doc = fitz.open("../../../Research Papers/~Domain-Specific Knowledge Graph Construction for Semantic Analysis.pdf")
# Total page in the pdf
print(len(doc))
# taking page for further processing
page = doc[0]

# list to store the co-ordinates of all highlights
highlights = []
# loop till we have highlight annotation in the page
annot = page.first_annot
while annot:
    if annot.type[0] == 8:
        all_coordinates = annot.vertices
        if len(all_coordinates) == 4:
            highlight_coord = fitz.Quad(all_coordinates).rect
            highlights.append(highlight_coord)
        else:
            all_coordinates = [all_coordinates[x:x+4] for x in range(0, len(all_coordinates), 4)]
            for i in range(0,len(all_coordinates)):
                coord = fitz.Quad(all_coordinates[i]).rect
                highlights.append(coord)
    annot = annot.next


all_words = page.get_text_words()


# List to store all the highlighted texts
highlight_text = []
for h in highlights:
    sentence = [w[4] for w in all_words if fitz.Rect(w[0:4]).intersect(h)]
    appended_words = " ".join(sentence)
    highlight_text.append(appended_words)
    print(appended_words)


