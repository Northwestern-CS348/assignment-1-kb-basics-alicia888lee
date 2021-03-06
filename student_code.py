import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))

        check = False

        for x in self.facts:
            if match(x.statement, fact.statement, None):
                check = True

        if check == False:
            if isinstance(fact, Fact):
                self.facts.append(fact)

        """
            add on somewhere: "if check == False, AND if fact isinstance "Fact"
        """

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """

        print("Asking {!r}".format(fact))

        """
            for x in the fact list:
                if fact matches x, print
                if it doesn't match do nothing
        """

        y=[]

        for x in self.facts:
            if match(x.statement, fact.statement, None):
                y.append(match(x.statement, fact.statement, None))

        """if length==0:
                return False
            else:
                return y"""

        if len(y) == 0:
            return False
        else:
            return y




