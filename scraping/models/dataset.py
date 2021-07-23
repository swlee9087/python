from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    bugs: object
    melon: object
    id: str
    label: str

    # gsttr. 구조체.
    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def bugs(self) -> object: return self._bugs

    @bugs.setter
    def bugs(self, bugs): self._bugs = bugs

    @property
    def melon(self) -> object: return self._melon

    @melon.setter
    def melon(self, melon): self._melon = melon

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
