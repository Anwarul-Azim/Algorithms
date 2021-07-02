"""

 simulated annealing search on one-dimensional objective function to find the better local minima 
 
"""
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

# 7 degree polynomial objective function 
def objective(p):
    # x and u for shifting the a templet function 
    x = p + 22 
    y = 0
    return (x**5)-(7* x**3)+(2* x**2)-(x**4)+(6*x)+(.005 * x**7) + y

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    best = bounds[:,0] + randn(len(bounds)) + (bounds[:,1] - bounds[:,0])
    best_eval = objective(best)
    curr, curr_eval = best, best_eval
    
    for i in range(n_iterations):
        candidate = curr + randn(len(bounds)) * step_size
        #candidate = best + randn() * step_size
        candidate_eval = objective(candidate)
        
        if(candidate_eval < best_eval):
            best, best_eval = candidate, candidate_eval
            print(i, best, best_eval)
        diff = candidate_eval - curr_eval
        t = float(temp/(i+1))
        metropolis = exp(-diff/t)
        if (diff<0 or metropolis < randn()):
            curr,curr_eval = candidate, candidate_eval        
                
    return [ best, best_eval]

	
	


seed(2)
# define range for input **most important hyperparameter
bounds = asarray([[-30, -21.0]])
# define the total iterations
n_iterations = 2000
# define the maximum step size
step_size = .01
# initial temperature ** another hyperparameter 
temp = 100

# perform the simulated annealing search
best, score = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Complete!')
print('f(%s) = %f' % (best, score))

