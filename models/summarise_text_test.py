# summarise_text("hello is this summarised?")

from summarise_text import summarise_text


def test_true_is_true():
    assert True is True

async def test_summarise_text_returns_not_nul():
  output = await summarise_text({
      "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres ",
  })
  assert output is not None

# def test_summarise_text_is_true():
#     output = summariseText({
#         "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres ",
#     })
#     assert output is not None