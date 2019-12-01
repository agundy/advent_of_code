defmodule Solutions.Day1 do
  def calculate_fuel(mass) do
    fuel =
      mass
      |> Kernel./(3)
      |> Kernel.trunc()
      |> Kernel.-(2)

    # Fuel has it's own weight and requires additional fuel to carry.
    if fuel > 0 do
      fuel + calculate_fuel(fuel)
    else
      0
    end
  end

  def answer(input) do
    ship_masses =
      File.stream!(input)
      |> Stream.map(&String.trim_trailing/1)
      |> Enum.to_list()

    # add all fuel costs up for the fleet
    Enum.reduce(ship_masses, 0, fn mass, acc ->
      mass
      |> String.to_integer()
      |> calculate_fuel
      |> Kernel.+(acc)
    end)
  end

  def answer do
    answer("data/day_1_input.txt")
  end
end
