from meta_brain_controller import MetaBrainController


print()
print("=== PM40 META BRAIN TEST ===")
print()

controller = MetaBrainController()

description = "strong trend breakout after pullback"

result = controller.analyze(description)

for k, v in result.items():

    print(k, ":", v)