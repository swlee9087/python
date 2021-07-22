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
    @property
    def fname(self) -> str: return self._fname
    @property
    def bugs(self) -> object: return self._bugs
    @property
    def melon(self) -> object: return self._melon
    @property
    def id(self) -> str: return self._id
    @property
    def label(self) -> str: return self._label
    @context.setter
    def context(self, context): self._context = context
    @fname.setter
    def fname(self, fname): self._fname = fname
    @bugs.setter
    def bugs(self, bugs): self._bugs = bugs
    @melon.setter
    def melon(self, melon): self._melon = melon
    @id.setter
    def id(self, id): self._id = id
    @label.setter
    def label(self, label): self._label = label
