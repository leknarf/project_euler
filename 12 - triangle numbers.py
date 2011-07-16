from __future__ import division

def factors(n):
    yield 1
    ii = 2
    while ii < n//2 + 1:
        if (n / ii) == int(n/ii):
            yield ii
        ii += 1
    yield n

# List retrieved from google
highly_composite_triangle_numbers = (1, 3, 6, 28, 36, 120, 300, 528, 630, 2016, 3240, 5460, 25200, 73920, 157080, 437580, 749700, 1385280, 1493856, 2031120, 2162160, 17907120, 76576500, 103672800, 236215980, 842161320, 3090906000, 4819214400, 7589181600, 7966312200, 13674528000, 20366564400, 49172323200, 78091322400, 102774672000, 557736444720, 666365279580, 876785263200, 1787835551040, 2427046221600, 3798207594720, 24287658595200, 26571463158240)

for hctn in highly_composite_triangle_numbers:
    if len(list(factors(hctn))) > 500:
        print(hctn)
        break