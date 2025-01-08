## Your Tasks

Restructure Newton’s method (_Case Study 3-2_) by decomposing it into three cooperating functions (including the original `newton` method.). The task of testing for the limit is assigned to a function named `limitReached`, whereas the task of computing a new approximation is assigned to a function named `improveEstimate`. Each function, in the file named **newton.py**, expects the relevant arguments and returns an appropriate value. (LO: 6.2)

Required methods to implement for this exercise:
```
    newton(x): Returns the square root of x
    improveEstimate(x, estimate): Returns the new estimate by using the formula (estimate + x / estimate) / 2
    limitReached(x, estimate): Returns True if the differences is less than or equal to the global TOLERANCE variable, else False
```
<!--
{
    "CopyExercise": {
        "name": "newton.py",
        "copyTarget": "/chapter6/ex01/student/newton.py",
        "pasteTarget": "/newton.py"
    }
}
-->

## Instructions
