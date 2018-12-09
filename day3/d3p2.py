claims = open("inputd3.txt")
# claims = open("sample_input_d3.txt")


CLOTH_SIZE = 1000
cloth = [[0]*CLOTH_SIZE for i in range(CLOTH_SIZE)]


def does_overlap(cloth, start_x, start_y, width, height):
    for x in range(start_x, start_x+width):
        for y in range(start_y, start_y+height):
            if cloth[x][y] >= 2:
                return True
    return False


for claim in claims:
    # 123 @ 3,2: 5x4
    delim_at = claim.find('@')
    delim_comma = claim.find(',')
    delim_colon = claim.find(':')
    delim_x = claim.find('x')
    start_x = int(claim[delim_at+2:delim_comma])  # avoid space
    start_y = int(claim[delim_comma+1:delim_colon])
    width = int(claim[delim_colon+2:delim_x])
    height = int(claim[delim_x+1:])
    for x in range(start_x, start_x+width):
        for y in range(start_y, start_y+height):
            cloth[x][y] += 1

# claims = open("sample_input_d3.txt")
claims = open("inputd3.txt")

for claim in claims:
    # 123 @ 3,2: 5x4
    delim_at = claim.find('@')
    delim_comma = claim.find(',')
    delim_colon = claim.find(':')
    delim_x = claim.find('x')
    start_x = int(claim[delim_at+2:delim_comma])  # avoid space
    start_y = int(claim[delim_comma+1:delim_colon])
    width = int(claim[delim_colon+2:delim_x])
    height = int(claim[delim_x+1:])
    if not does_overlap(cloth, start_x, start_y, width, height):
        claim_id = int(claim[1:delim_at - 1])
        print(claim_id)
