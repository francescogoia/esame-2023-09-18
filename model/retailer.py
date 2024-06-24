from dataclasses import dataclass


@dataclass
class Retailer:
    Retailer_code: str
    Retailer_name: str

    def __hash__(self):
        return hash(self.Retailer_code)

    def __str__(self):
        return f"{self.Retailer_code} - {self.Retailer_name}"

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code