from browser import document, display

def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = ""
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    display("SKU: ", sku, target='sku_output')

def create_order(e):
    # Connect your custom pet items using safe prod1-prod5 variables
    prod1 = document.getElementById("Beetles")
    prod2 = document.getElementById("Snails")
    prod3 = document.getElementById("Chicken Bones")
    prod4 = document.getElementById("Meat trimmings")
    prod5 = document.getElementById("Premium goldfish")
    
    # Calculate subtotal using safe names (no illegal spaces)
    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)
                
    tax_rate = 0.12  # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # Build your text invoice block
    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """
    
    # Push the receipt out onto your screen container
    document.getElementById("show").innerHTML = receipt