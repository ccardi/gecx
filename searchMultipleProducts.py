def searchMultipleProducts(queries: list[str]) -> dict:
    config = context.state.get("config_vaisc")
    print(config)
    # This will hold the final array of objects for our schema
    query_results = []
    
    for query in queries:
        # Create a brand new local dictionary for each specific query
        local_config = {**config, "query": query}
        results = tools.search_commerce_Search(local_config)
        data = results.json()
        
        product_details = []
        for e in data.get("results", [])[:50]:
            product_data = e.get("product", {})
            images = product_data.get("images", [])
            
            # Extract price safely
            price_info = product_data.get("priceInfo", {})
            price_val = price_info.get("price", "N/A")
            price_currency = price_info.get("currencyCode", "N/A")

            product_details.append({
                "productId": e.get("id"),
                "title": product_data.get("title", "")[:40],
                "uri": product_data.get("uri"),
                # Only take index 0 if the list isn't empty
                "imageUris": [images[0]["uri"]] if images else [],
                "price": f"{price_val} {price_currency}" # Assuming GDB was meant to be GBP, adjust if needed
            })
            
        # Append this query's block to the main list
        query_results.append({
            "query": query,
            "productDetails": product_details
        })

    # Return the dictionary exactly matching the updated schema root
    return {"queries": queries, "queryResults": query_results, "type": "products-carousels"}