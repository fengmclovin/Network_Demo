import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1); // Initialize with an invalid index
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                stack.push(i); // Push the index of '(' into the stack
            } else {
                stack.pop(); // Pop the top index as '(' is matched
                if (stack.isEmpty()) {
                    stack.push(i); // Push the current index as a new starting point
                } else {
                    maxLen = Math.max(maxLen, i - stack.peek()); // Update maxLen
                }
            }
        }
        
        return maxLen;
    }
}
