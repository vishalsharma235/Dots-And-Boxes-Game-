###################################
### 
### Minimax class to create Minimax() objects
### used by AI to determine next move.
###
################


from board import Board

class Minimax(object):
    
    def minMax(self, root, search_depth, alpha=float("-inf"), beta=float("inf")): 
        root.getChildren()
        if (root.depth >= search_depth) or (len(root.children) == 0):
            return root.score
        if root.player == 1:
            bestValue = float("-inf")
            for child in root.children:
                value = self.minMax(child, (search_depth-1), alpha, beta)
                if value > bestValue: 
                    bestValue = value
                if bestValue > alpha:
                    alpha = bestValue
                if beta <= alpha:
                    break
            root.value = bestValue
            return bestValue
        
        elif root.player == -1:
            bestValue = float("inf")
            for child in root.children:
                value = self.minMax(child, (search_depth-1), alpha, beta)
                if value < bestValue:
                    bestValue = value
                if bestValue < beta:
                    beta = bestValue
                if beta <= alpha:
                    break
            root.value = bestValue
            return bestValue
    
    def bestMove(self, root, search_depth):
        root = root.copy()
        best = self.minMax(root, search_depth, float("-inf"), float("inf"))
        for child in root.children:
            if child.value == best:
                move = child.move
                return move
            move = child.move
        return move
        
