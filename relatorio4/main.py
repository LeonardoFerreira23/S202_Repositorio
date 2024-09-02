from pymongo import MongoClient

class ProductAnalyzer:
    def __init__(self, database, collection):
        self.client = MongoClient('mongodb://localhost:27017/')  
        self.db = self.client[database]
        self.collection = self.db[collection]

    def total_sales_by_day(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ]
        result = self.collection.aggregate(pipeline)
        return list(result)

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ]
        result = self.collection.aggregate(pipeline)
        return list(result)

    def top_spending_customer(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        result = self.collection.aggregate(pipeline)
        return list(result)

    def products_with_quantity_above_one(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_quantidade": {"$gt": 1}}}
        ]
        result = self.collection.aggregate(pipeline)
        return list(result)

if __name__ == "__main__":
    analyzer = ProductAnalyzer(database="mercado", collection="produtos")

    print("Total de vendas por dia:")
    print(analyzer.total_sales_by_day())

    print("\nProduto mais vendido:")
    print(analyzer.most_sold_product())

    print("\nCliente que mais gastou em uma única compra:")
    print(analyzer.top_spending_customer())

    print("\nProdutos vendidos em quantidade acima de 1 unidade:")
    print(analyzer.products_with_quantity_above_one())