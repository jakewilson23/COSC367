## ⍺-𝛽 pruning
In an alpha-beta pruning question you are given an explicit game tree (where either max is playing at root or min) and then asked to prune the tree. You need to provide two variables: pruned_tree which is the pruned game tree and pruning_events which is a list of pairs of alpha and beta when a pruning event was triggered. Please keep the following points in mind:

- It might be easier to answer this question by drawing the tree.
- Process the children of a node from left to right.
- A pruning event is triggered when alpha becomes greater than or equal to beta.
- Children of a node are processed from left to right.
- A pruning event might be triggered without any branches getting pruned. This happens when the event is triggered after seeing the last child. Such events must also be included in the list.
- For some problems the pruned tree is the same as the original tree (i.e. no pruning) even if there have been some pruning events.
- You do not need to provide any function in your answer, however, if you wish, you can write a program to compute the requested variables automatically.