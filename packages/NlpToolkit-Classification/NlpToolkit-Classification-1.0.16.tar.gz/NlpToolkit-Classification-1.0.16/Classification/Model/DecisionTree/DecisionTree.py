from Classification.Instance.CompositeInstance import CompositeInstance
from Classification.Instance.Instance import Instance
from Classification.InstanceList.InstanceList import InstanceList
from Classification.Model.DecisionTree.DecisionNode import DecisionNode
from Classification.Model.ValidatedModel import ValidatedModel


class DecisionTree(ValidatedModel):

    __root: DecisionNode

    def constructor1(self, root: DecisionNode):
        """
        Constructor that sets root node of the decision tree.

        PARAMETERS
        ----------
        root : DecisionNode
            DecisionNode type input.
        """
        self.__root = root

    def constructor2(self, fileName: str):
        inputFile = open(fileName, mode='r', encoding='utf-8')
        self.__root = DecisionNode(inputFile)
        inputFile.close()

    def __init__(self, root: object):
        if isinstance(root, DecisionNode):
            self.constructor1(root)
        elif isinstance(root, str):
            self.constructor2(root)

    def predict(self, instance: Instance) -> str:
        """
        The predict method  performs prediction on the root node of given instance, and if it is null, it returns the
        possible class labels. Otherwise it returns the returned class labels.

        PARAMETERS
        ----------
        instance : Instance
            Instance make prediction.

        RETURNS
        -------
        str
            Possible class labels.
        """
        predicted_class = self.__root.predict(instance)
        if predicted_class is None and isinstance(instance, CompositeInstance):
            predicted_class = instance.getPossibleClassLabels()
        return predicted_class

    def predictProbability(self, instance: Instance) -> dict:
        return self.__root.predictProbabilityDistribution(instance)

    def pruneNode(self,
                  node: DecisionNode,
                  pruneSet: InstanceList):
        """
        The prune method takes a DecisionNode and an InstanceList as inputs. It checks the classification performance
        of given InstanceList before pruning, i.e making a node leaf, and after pruning. If the after performance is
        better than the before performance it prune the given InstanceList from the tree.

        PARAMETERS
        ----------
        node : DecisionNode
            DecisionNode that will be pruned if conditions hold.
        pruneSet : InstanceList
            Small subset of tree that will be removed from tree.
        """
        if node.leaf:
            return
        before = self.testClassifier(pruneSet)
        node.leaf = True
        after = self.testClassifier(pruneSet)
        if after.getAccuracy() < before.getAccuracy():
            node.leaf = False
            for child in node.children:
                self.pruneNode(child, pruneSet)

    def prune(self, pruneSet: InstanceList):
        """
        The prune method takes an InstanceList and  performs pruning to the root node.

        PARAMETERS
        ----------
        pruneSet : InstanceList
            InstanceList to perform pruning.
        """
        self.pruneNode(self.__root, pruneSet)
