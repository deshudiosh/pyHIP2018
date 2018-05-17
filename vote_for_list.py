list = [["Harmony in Motion", "Wall Covering: Contract", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10916", 1080],
        ["Tauko Stool", "Seating: Residential/Stool","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10268", 280],
        ["Hybrid Collection Mesh Pattern ", "Materials, Treatments and Surfaces","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10760", 662],
        ["Drum Teen", "Seating: Residental/Accent","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8545", 850],
        ["Tauko Modular Table", "Furniture: Contract/Tables", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10104", 762],
        ["Tauko Modular Table", "Furniture: Education", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10262", 338],
        ["Harmony in Motion", "Wall Covering: Paper", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9569", 174],
        ["Tapa", "Seating: Contract/Lounge", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10270", 558],
        ["River Snake", "Furniture: Outdoor", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/7775", 550]]

others = [['3', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10649', 400],
            ['4', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10503', 400],
            ['5', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9606', 400],
            ['6', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9864', 400],
            ['7', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10074', 400],
            ['8', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10934', 400],
            ['9', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10604', 400],
            ['10', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8237', 400],
            ['11', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9110', 400],
            ['12', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9491', 400],
            ['13', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9618', 400],
            ['14', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/7677', 400],
            ['15', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10057', 400],
            ['16', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8170', 400],
            ['17', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9637', 400],
            ['18', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8749', 400],
            ['19', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10138', 400],
            ['20', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10697', 400],
            ['21', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8223', 400],
            ['22', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10559', 400],
            ['23', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10050', 400],
            ['24', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9443', 400],
            ['25', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8175', 400],
            ['26', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/7523', 400],
            ['27', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9839', 400],
            ['28', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9667', 400],
            ['29', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10690', 400],
            ['30', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8771', 400],
            ['31', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10930', 400],
            ['32', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10428', 400],
            ['33', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9837', 400],
            ['34', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/11154', 400],
            ['35', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9431', 400],
            ['36', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9430', 400],
            ['37', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10239', 400],
            ['38', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/7658', 400],
            ['39', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9837 ', 400],
            ['40', '', 'https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8170', 400]]


test_list = [["nazwa", "categoria", "url", 1],
             ["nazwa2", "categoria2", "url2", 2]]

def get_project_list():
    return [{"name": e[0], "category": e[1], "url": e[2], "num_iter": e[3]} for e in others]


