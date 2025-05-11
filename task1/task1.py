from pathlib import Path

def total_salary(path: str) -> tuple[int, int]:
    """
    Calculates the total and average salary of developers from a given text file.

    Each line in the file should contain a developer's surname and their salary, separated by a comma.
    Example line: "Alex Korp,3000"

    Parameters:
        path (str): The file path to the salary data file.

    Returns:
        tuple: A tuple (total_salary, average_salary) where:
            - total_salary (int): Sum of all salaries.
            - average_salary (int): Average salary. Returns 0 if no valid data is found.

    Exceptions:
        If the file is not found or another error occurs, the function prints an error message and returns (0, 0).
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                # Remove leading/trailing whitespace and split by comma
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # Skip invalid lines

                try:
                    salary = float(parts[1])  # Convert salary to float
                    salaries.append(salary)
                except ValueError:
                    continue  # Skip lines with invalid salary value

            if not salaries:
                return (0, 0)

            total_salary_amount = sum(salaries)
            average_salary = total_salary_amount / len(salaries)
            return (int(total_salary_amount), int(average_salary))

    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    except OSError  as e:
        print(f"File error: {e}")
        return (0, 0)

# Construct the absolute path to the file
current_dir = Path(__file__).parent
file_path = current_dir / "salary_file.txt"

# Calculate total and average salary
total_amount, avg_salary = total_salary(str(file_path))
print(f"The legal amount of salary: {total_amount}, Average salary: {avg_salary}")