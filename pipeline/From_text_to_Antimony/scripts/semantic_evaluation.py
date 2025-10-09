import re
import os
import pandas as pd

### Snakemake ###
in_file = snakemake.input[0]
out_file = snakemake.output[0]


# evaluation of the number of reactions,floating species, boundary species, compartments:

rere = re.compile(r"""^\s*(?:(?P<id>[A-Za-z_]\w*)(?:\s+in\s+(?P<comp>[A-Za-z_]\w*))?\s*:)?\s*(?P<lhs>[^;\r\n]*?)\s*(?P<arrow><->|->|=>)\s*(?P<rhs>[^;\r\n]*?)\s*;\s*(?P<rate>[^;\r\n]*\S[^;\r\n]*)\s*$""", re.X)

reboundarysp = re.compile(r"(?:(?<=species\s)|(?<=,\s))(\$\w+)(?=\sin\s[A-Za-z0-9_.]+)")

refloatsp = re.compile(r"(?:(?<=species\s)|(?<=,\s))(?<!\$)\b([A-Za-z0-9_.]+)\b(?=\s+in\s+[A-Za-z0-9_.]+)", re.X)

reCompart = re.compile(r"(?<=compartment\s)\b[a-zA-Z0-9_]+(?=,|;)|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*compartment\s)|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*species)", re.X)

#Gl_pattern = re.compile(r"(?<=\/\/ Variable initializations:\n\s\s)([a-zA-Z0-9_]+)\s=\s([a-zA-Z0-9_]+);", re.X)

with open(in_file) as f:
    text = f.read()

Boundsp = re.findall(reboundarysp, text)
Floatsp = re.findall(refloatsp, text)
Comps = re.findall(reCompart, text)

                
reactions = []

with open(in_file) as f:
    for l in f:
            p1=rere.search(l)
            if p1 is not None:
                reactions.append(p1.group())
            
# result


#print(f"Found: {len(Boundsp)} Boundary species\nFound: {len(Floatsp)} Floating species.\nFound: {len(reactions)} reactions\nFound: {len(Comps)} compartments")


# table creation:     antimony_model | num Boundary sp. | num Floating sp | num reactions | num Compartments |

data= {
     "N° Boundary sp.": len(Boundsp),
     "N° Floating sp.": len(Floatsp),
     "N° Reactions": len(reactions),
     "N° Compartments":len(Comps),
     "N° Glob.Parameters": "TBD",
}

filename = os.path.basename(in_file)

df = pd.DataFrame(data, index=[filename])

# Output CSV 

df.to_csv(out_file)

          
     











# corrected for boundary detection through ReGex: "^(\s*species\s[\w]+\s[in])|(\b,\s[\w]+\s[in])"mg

# this regex code extract all the floating species but it counts all the occurrences, so after the extraxtion use a set in order to keep each species once and then transform it in a list.
### "(?!\s*species\s)([$][\w]+)|([$][\w]+)(?!\s\bin\b)"gm

# this is the regex code to extract floating species: "/(?<=species\s)(?<!\$)\b([A-Za-z0-9_.]+)\b(?=\s+in\s+[A-Za-z0-9_.]+)|(?<=,\s)(?<!\$)\b([A-Za-z0-9_.]+)\b(?=\s+in\s+[A-Za-z0-9_.]+)/gm"

# this is the regex code to extract boundary species: "/(?<=species\s)(\$\w+)(?=\sin\s[A-Za-z0-9_.]+)|(?<=,\s)((?1))(?=\sin\s[A-Za-z0-9_.]+)/gm"

#this is the code regex to find out the compartment : /(?<=compartment\s)\b[a-zA-Z0-9_]+(?=,|;)|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*(compartment\s))|(?<=,\s)\b[a-zA-Z0-9_]+(?=;\n\s*species)/gm ne ho un altra # (?<=compartment\s)\b[a-zA-Z0-9.]+|(?<=,\s)\b[a-zA-Z0-9.]+(?=,|;) ; (?<=compartment\s)\b.+[^,](?=;)

# for the Global parameter I have to use three regex: un to split the section //Variable initializations, the second one to extract the values, a third one to extract the paramenters defined 
# in the //Other Declarations: section and the last regex to extract the element "var".

# first: /(?<=\/\/ Variable initializations:\n)([\s\S]*?)(?=\n\s*\/\/)/gm
# second: /(?<=\s\s)([a-zA-Z0-9_\/]+)(?=\s=)|(?<=;\n\s\s)([a-zA-Z0-9_\/]+)(?=\s=)/gm
## third: /(?<=\bvar\b)([\s\S]*?)(?=;\n\s*const)/gm    serve per prendere tutte le istanze tra il primo simbolo var fino a const
##fourth: /(?<=\s|,\s)([a-zA-Z0-9_]+[^,;])(?=,|;|\bvar\b)|(?<=\s)([a-zA-Z0-9_]+)$/gm recupera tutti gli elementi dall'ultima estrazione (global parameters della sezione Other Declaration)


# third: /(?<=\bvar\b)([\s\S]*?)(?=;\n)/gm
#fouth: /(?<=\s|,)([a-zA-Z0-9_]+[^,;])(?=,|;|)/gm

#initializatior
"""
reactions = []
Floatsp = []
Boundsp = []
Comparts = []

with open('orBIOMD300.txt') as f:
    for l in f:
            p1=rere.search(l)
            p2=reboundarysp.search(l)
            p3=refloatsp.search(l)
            p4=reCompart.search(l)
            if p1 is not None:
                    reactions.append(p1.group())
            if p2 is not None:
                    Boundsp.append(p2.group())
            if p3 is not None:
                    Floatsp.append(p3.group())
            if p4 is not None:
                    Comparts.append(p4.group())

numFloating=len(Floatsp)
numBoundary=len(Boundsp)
numComparts=len(Comparts)
numReacts=len(reactions)

print(Boundsp)
"""
#pattern = re.compile(r"(?:(?<=compartment\s)|(?<=,\s))\b\w+\b(?=,|;)")
#reCompart = re.compile(r"(?:(?<=compartment\s)|(?<=,\s))\b[a-zA-Z0-9_]+(?=,|;\n\r\s\scompartment|;\n\r\s\sspecies)")