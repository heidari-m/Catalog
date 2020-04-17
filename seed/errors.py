from django.forms.utils import ErrorList


class SpaceProhibited(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error"> <span class="red-text">%s</span></div>' % e for e in self])