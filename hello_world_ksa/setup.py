from setup import setup, find_namespace_packages

setup(name='hello_world_ksa',
      version='0.0.1',
      description='Our first package',
      author='Karinocka',
      author_email='ondatra410@.com',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['greeting=hello_world_ksa.main:hello_world']}
)

# greeting - команда, яка повинна виконатись у терміналі
# після '=' пишемо шлях до файлу, де знаходиться функція => hello_world_vvm.main
# після ':' пишемо назву функції greeting