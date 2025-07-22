# motorin_screener_items.py

motorin_items = [
    {
        "age_range": "6-12 Months",
        "color": "light blue",
        "items": [
            "Reaches with both hands",
            "Transfers toy hand-to-hand",
            "Uses whole hand to rake small objects",
            "Bangs objects together",
            "Brings hands to midline",
            "Scribbles spontaneously when given a crayon",
            "Fisted grasp when holding a crayon"
        ]
    },
    {
        "age_range": "12-18 Months",
        "color": "orange",
        "items": [
            "Points with index finger",
            "Releases small object into container voluntarily",
            "Stacks 2–3 blocks",
            "Turns pages in a cardboard book",
            "Uses a spoon with spills",
            "Pulls lids off containers (e.g., Play-Doh, Tupperware)",
            "Digital pronate grasp when coloring"
        ]
    },
    {
        "age_range": "18-24 Months",
        "color": "light blue",
        "items": [
            "Imitates vertical stroke with crayon",
            "Places small objects into a container",
            "Builds a 4-block tower",
            "Opens Ziplock bags"
        ]
    },
    {
        "age_range": "24-30 Months",
        "color": "orange",
        "items": [
            "Imitates horizontal stroke",
            "Turns single pages in board books",
            "Unscrews lids from containers",
            "Snips with child-safe scissors",
            "Scribbles within large shapes without crossing boundaries",
            "Attempts to copy a circle",
            "Uses fingertip grasp when coloring"
        ]
    },
    {
        "age_range": "30-36 Months",
        "color": "light blue",
        "items": [
            "Copies circle independently",
            "Begins to draw a person with head and limbs (2–4 parts)",
            "Builds 6–8 block tower",
            "Uses spoon and fork with moderate spill",
            "Tripod grasp emerges when coloring"
        ]
    },
    {
        "age_range": "3-4 Years",
        "color": "orange",
        "items": [
            "Copies cross",
            "Cuts across a piece of paper with scissors",
            "Strings large beads",
            "Buttons large buttons",
            "Begins drawing a square"
        ]
    },
    {
        "age_range": "4-5 Years",
        "color": "light blue",
        "items": [
            "Copies square",
            "Begins drawing triangle",
            "Cuts on a line with scissors",
            "Writes some letters in their name",
            "Dresses self with supervision (zippers/buttons)"
        ]
    },
    {
        "age_range": "5-6 Years",
        "color": "orange",
        "items": [
            "Copies triangle",
            "Begins copying diamond",
            "Draws person with 6+ parts",
            "Prints first and last name",
            "Ties shoelaces (attempts)",
            "Buttons and unbuttons without help"
        ]
    },
    {
        "age_range": "6-7 Years",
        "color": "light blue",
        "items": [
            "Copies diamond",
            "Writes legibly within lines",
            "Cuts out complex shapes accurately",
            "Ties shoelaces independently",
            "Demonstrates refined tripod grasp"
        ]
    }
]

# Example usage
if __name__ == "__main__":
    for section in motorin_items:
        print(f"Age: {section['age_range']} ({section['color']})")
        for item in section['items']:
            print(f"  - {item}")
        print()
