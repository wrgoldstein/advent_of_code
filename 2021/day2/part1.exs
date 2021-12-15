sample_input = "forward 5
down 5
forward 8
up 3
down 8
forward 2" |> String.split("\n")

sample_input
  |> Enum.reduce([0, 0], fn x, [position, depth] -> 
    case x do
      "forward " <> y ->
        [position + String.to_integer(y), depth]
      "down " <> y ->
        [position, depth + String.to_integer(y)]
      "up " <> y ->
        [position, depth - String.to_integer(y)]
    end
  end) 
  |> Enum.product
  |> IO.puts