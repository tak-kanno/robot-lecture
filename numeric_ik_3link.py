import numpy as np
import matplotlib.pyplot as plt

class NumericIK:
    def __init__(self):
        self.l_1 = 200
        self.l_2 = 200
        self.l_3 = 200

    def forward_kinematics(self, q):
        x = self.l_1 * np.cos(q[0]) + self.l_2 * np.cos(q[0] + q[1]) + self.l_3 * np.cos(q[0] + q[1] + q[2])
        y = self.l_1 * np.sin(q[0]) + self.l_2 * np.sin(q[0] + q[1]) + self.l_3 * np.sin(q[0] + q[1] + q[2])
        theta = q[0] + q[1] + q[2]
        return np.array([x, y, theta])

    def numerical_jacobian(self, q):
        delta = 0.0001
        J = np.zeros((3, 3))
        for i in range(3):
            q_delta = np.copy(q)
            q_delta[i] += delta
            x_delta = self.forward_kinematics(q_delta)
            J[:, i] = (x_delta - self.forward_kinematics(q)) / delta
        return J

    def draw_links(self, q, x_d, i):
        x = np.array([0, self.l_1 * np.cos(q[0]), self.l_1 * np.cos(q[0]) + self.l_2 * np.cos(q[0] + q[1]), self.l_1 * np.cos(q[0]) + self.l_2 * np.cos(q[0] + q[1]) + self.l_3 * np.cos(q[0] + q[1] + q[2])])
        y = np.array([0, self.l_1 * np.sin(q[0]), self.l_1 * np.sin(q[0]) + self.l_2 * np.sin(q[0] + q[1]), self.l_1 * np.sin(q[0]) + self.l_2 * np.sin(q[0] + q[1]) + self.l_3 * np.sin(q[0] + q[1] + q[2])])

        # clear the plot
        plt.clf()
        
        # Draw links
        plt.plot(x, y, marker='o', color='k', linestyle='-', linewidth=2)

        # Draw target position
        plt.scatter(x_d[0], x_d[1], s=100, c='red', marker='x')

        # Write the frame number
        plt.text(0, 500, 'i= {}'.format(i), fontsize=10)

        # Set the plot as square
        plt.axis('square')
        
        # x and y axis range
        plt.xlim(-50, 600)
        plt.ylim(-50, 600)

        # Write animation frames to files
        plt.savefig('frames_3/{}.png'.format(i))

    def solve(self, target_position, initial_q, beta, epsilon):
        q = initial_q
        i = 0

        # Draw initial links
        self.draw_links(q, target_position, i)
        i += 1

        while True:
            # Calculate forward kinematics
            x = self.forward_kinematics(q)
            # Calculate Jacobian Inverse
            # J_inv = np.linalg.inv(jacobian(q))
            J_inv = np.linalg.inv(self.numerical_jacobian(q))
            # Use pseudo inverse if inverse is not available
            # J_inv = np.linalg.pinv(jacobian(q))

            # Calculate position error
            e = target_position - x
            # Update joint angle vector
            q = q + beta * np.dot(J_inv, e)

            # Print joint angles
            print('q1: {}, q2: {}, q3: {}'.format(np.rad2deg(q[0]), np.rad2deg(q[1]), np.rad2deg(q[2])))

            # Draw links
            self.draw_links(q, target_position, i)
            i += 1

            # Check if the position error is small enough
            if np.linalg.norm(e) < epsilon:
                break

        return q


if __name__ == '__main__':

    # Set the target position
    target_position = np.array([450, 50, np.deg2rad(-45)])

    # Set the initial joint angle vector
    initial_q = np.array([np.deg2rad(10), np.deg2rad(-10), np.deg2rad(1)])

    # Set the calculation gain
    beta = 0.1

    # Set the termination condition
    epsilon = 0.01

    # Solve the inverse kinematics
    numeric_ik = NumericIK()
    q = numeric_ik.solve(target_position, initial_q, beta, epsilon)

    # Print the final joint angles
    print('q1: {}, q2: {}'.format(np.rad2deg(q[0]), np.rad2deg(q[1])))

