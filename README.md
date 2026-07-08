
# PRODIGY_ST_01 - Calculator Application Test Cases

## Task Description
Write detailed test cases for a Simple Calculator Application. Cover valid inputs, invalid inputs, and edge cases for addition, subtraction, multiplication, and division.

## Test Cases

### TC001: Addition of Two Positive Numbers
**Test Case ID**: TC001  
**Test Description**: Verify addition of two positive numbers  
**Preconditions**: Calculator application is launched  
**Test Steps**: 
1. Enter 15 in first input field
2. Select + operator
3. Enter 25 in second input field
4. Click = button  
**Expected Result**: Result should display 40

### TC002: Subtraction with Negative Result
**Test Case ID**: TC002  
**Test Description**: Verify subtraction resulting in negative value  
**Preconditions**: Calculator application is launched  
**Test Steps**:
1. Enter 10
2. Select - operator
3. Enter 30
4. Click =  
**Expected Result**: Result should display -20

### TC003: Multiplication of Decimal Numbers
**Test Case ID**: TC003  
**Test Description**: Verify multiplication with decimal values  
**Preconditions**: Calculator application is launched  
**Test Steps**:
1. Enter 5.5
2. Select * operator
3. Enter 2
4. Click =  
**Expected Result**: Result should display 11.0

### TC004: Division by Zero
**Test Case ID**: TC004  
**Test Description**: Verify system handles division by zero  
**Preconditions**: Calculator application is launched  
**Test Steps**:
1. Enter 50
2. Select / operator
3. Enter 0
4. Click =  
**Expected Result**: Error message "Cannot divide by zero" should be displayed

### TC005: Invalid Input - Alphabets
**Test Case ID**: TC005  
**Test Description**: Verify system rejects non-numeric input  
**Preconditions**: Calculator application is launched  
**Test Steps**:
1. Enter abc
2. Select + operator
3. Enter 10
4. Click =  
**Expected Result**: Error message "Invalid input" should be displayed

### TC006: BODMAS Rule Check
**Test Case ID**: TC006  
**Test Description**: Verify calculator follows operator precedence  
**Preconditions**: Calculator application is launched  
**Test Steps**:
1. Enter 10 + 5 * 2
2. Click =  
**Expected Result**: Result should display 20
