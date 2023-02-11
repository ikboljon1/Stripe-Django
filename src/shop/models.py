from django.db import models


class Item(models.Model):
    """Модель элемента, представляющая один элемент на сайте. Как хранение."""

    item_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=64, verbose_name="Название элемента для отображения"
    )  # About ~=64 characters long.
    description = models.TextField(verbose_name="Описание элемента для отображения")
    # May be decimal field.
    price = models.IntegerField(
        verbose_name="Цена товара на кассе (/100!) 250 => 2.5$"
    )

    def get_display_price(self) -> float:
        """Returns display price (as model price is stripe-like format price)"""
        return self.price / 100

    def get_display_title(self) -> str:
        return f"{self.name} (Item №{self.item_id})"

    def __str__(self):
        return self.get_display_title()

    def __repr__(self):
        return self.get_display_title()
