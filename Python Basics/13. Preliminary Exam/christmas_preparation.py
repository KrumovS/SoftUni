papers = int(input())
rolls = int(input())
glue = float(input())
discount = int(input())

paper_price = 5.80
rolls_price = 7.20
glue_price = 1.20
discount = (100 - discount) / 100

total_papers_price = papers * paper_price
total_rolls_price = rolls * rolls_price
total_glue_price = glue * glue_price

total_amount = (total_papers_price + total_rolls_price + total_glue_price) * discount

print(f'{total_amount:.3f}')
