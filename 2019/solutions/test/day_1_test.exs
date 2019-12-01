defmodule SolutionsDay1Test do
  use ExUnit.Case
  alias Solutions.Day1

  test "calculates fuel for mass 12" do
    assert Day1.calculate_fuel(12) == 2
  end

  test "calculates fuel for 1969" do
    assert Day1.calculate_fuel(1969) == 966
  end

  test "calculates fuel for 100756" do
    assert Day1.calculate_fuel(100_756) == 50346
  end
end
