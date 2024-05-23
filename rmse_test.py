import rmse

def test_rmse():
    predictions = [1, 2, 3, 4, 5]
    targets = [1, 2, 3, 4, 5]

    result = rmse.rmse(predictions, targets)
    print(f"Test 1 - Predictions: {predictions}, Targets: {targets}, RMSE: {result}")
    assert result == 0, f"Expected RMSE: 0, but got: {result}"

    predictions = [2, 3, 4, 5, 6]
    targets = [1, 2, 3, 4, 5]

    result = rmse.rmse(predictions, targets)
    print(f"Test 2 - Predictions: {predictions}, Targets: {targets}, RMSE: {result}")
    assert result == 1, f"Expected RMSE: 1, but got: {result}"

if __name__ == "__main__":
    test_rmse()

