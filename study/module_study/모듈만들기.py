import pay_module

print(pay_module.version)

pay_module.print_author()

pay_info = pay_module.Pay("A13145", 13000, "2024-08-30")
print(pay_info.get_pay_info())

print(pay_module.__name__)
print(pay_module.__file__)
