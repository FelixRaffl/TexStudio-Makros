import json
import os

macros_data = {
    "Figure": {
        "abbrev": "",
        "description": "Standard Figure",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Figure",
        "shortcut": "",
        "tag": [
            "\\begin{figure}[H]",
            "\t\\centering",
            "\t\\includegraphics[width=%<1\\textwidth%>]{%<Grafiken/pfad.pdf%>}",
            "\t\\caption{%<Caption%>}",
            "\t\\label{fig:%<label%>}",
            "\\end{figure}",
            "%|"
        ],
        "trigger": "@fig"
    },
    "Table": {
        "abbrev": "",
        "description": "Standard Table with footnotesize",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Table",
        "shortcut": "",
        "tag": [
            "\\begin{table}[H]",
            "\t\\centering",
            "\t\\caption{%<Caption%>}",
            "\t\\label{tab:%<label%>}",
            "\t\\footnotesize ",
            "\t\\begin{tabular}{%<ll%>}",
            "\t\\hline",
            "\t%<Header 1%> & %<Header 2%> \\\\ \\hline",
            "\t%| & \\\\",
            "\t\\hline",
            "\t\\end{tabular}",
            "\\end{table}"
        ],
        "trigger": "@tab"
    },
    "Double_Figure": {
        "abbrev": "",
        "description": "Two Side-by-Side Figures with Minipages",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Double Figure",
        "shortcut": "",
        "tag": [
            "\\begin{figure}[H]",
            "\t\\centering",
            "\t\\begin{minipage}[t]{0.48\\textwidth}",
            "\t\t\\centering",
            "\t\t\\includegraphics[height=\\textwidth]{%<Grafiken/pfad1.pdf%>}",
            "\t\\end{minipage}",
            "\t\\hfill",
            "\t\\begin{minipage}[t]{0.48\\textwidth}",
            "\t\t\\centering",
            "\t\t\\includegraphics[height=\\textwidth]{%<Grafiken/pfad2.pdf%>}",
            "\t\\end{minipage}",
            "\t\\caption[%<Kurzes Caption für Verzeichnis%>]{%<Langes Caption%>}",
            "\t\\label{fig:%<label%>}",
            "\\end{figure}",
            "%|"
        ],
        "trigger": "@doublefig"
    },
    "Code_Listing": {
        "abbrev": "",
        "description": "Code snippet in centered minipage",
        "formatVersion": 1,
        "menu": "Custom",
        "name": "Code Listing",
        "shortcut": "",
        "tag": [
            "\\begin{center}",
            "\t\\begin{minipage}{0.9\\linewidth}",
            "\t\\begin{lstlisting}[caption={%<Caption%>}, label={code:%<label%>}]",
            "\t%|",
            "\t\\end{lstlisting}",
            "\t\\end{minipage}",
            "\\end{center}"
        ],
        "trigger": "@code"
    }
}

# Ordnername definieren
folder_name = "Macros"

# Ordner erstellen, falls er nicht existiert
os.makedirs(folder_name, exist_ok=True)

# Generiert eine separate Datei für jedes Macro im neuen Ordner
for filename, file_content in macros_data.items():
    # Pfad zusammensetzen (Ordner + Dateiname)
    full_filename = os.path.join(folder_name, f"{filename}.txsMacro")
    
    with open(full_filename, "w", encoding="utf-8") as f:
        json.dump(file_content, f, indent=4)
        
    print(f"Erfolgreich erstellt: {full_filename}")

print(f"\nAlle Dateien wurden generiert und im Ordner '{folder_name}' gespeichert!")