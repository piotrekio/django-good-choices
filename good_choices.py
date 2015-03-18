import collections
import inspect
import six


__all__ = ['Choices', 'VERSION']

VERSION = (1, 4)


class ChoicesMeta(type):
    def __new__(cls, name, bases, attrs):
        ch = list()
        updated_attrs = dict()
        labels = {}
        for attr_name, attr_value in six.iteritems(attrs):
            if not attr_name.startswith('_'):
                try:
                    index, label = attr_value
                except (ValueError, TypeError):
                    index = label = attr_value
                ch.append((index, label))
                labels[index] = label
                updated_attrs[attr_name] = index
        attrs.update(updated_attrs)
        attrs['choices'] = sorted(ch, key=lambda c: c[0] or '')
        attrs['labels'] = labels
        return super(ChoicesMeta, cls).__new__(cls, name, bases, attrs)

    def __iter__(self):
        for index, label in self.choices:
            yield index


@six.add_metaclass(ChoicesMeta)
class Choices(object):
    pass


class Registry(object):
    def __init__(self):
        self.registry = collections.defaultdict(dict)

    def register(self, choices_class, namespace=None):
        self.registry[namespace][choices_class.__name__] = choices_class

registry = Registry()
