import json
 class Status:
    def __init__(self):
        self.status_file = 'status.json'
        self.status = self.load_status()

    def load_status(self):
        try:
            with open(self.status_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'total_sales': 0,
                'total_customers': 0,
                'products_sold': {}
            }

    def save_status(self):
        with open(self.status_file, 'w') as f:
            json.dump(self.status, f, indent=4)

    def update_sales(self, product_name, quantity):
        self.status['total_sales'] += quantity
        self.status['total_customers'] += 1
        if product_name in self.status['products_sold']:
            self.status['products_sold'][product_name] += quantity
        else:
            self.status['products_sold'][product_name] = quantity
        self.save_status()