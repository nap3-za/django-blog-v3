from django import forms


status = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

categories = (
    ('general', 'General'),
    ('technology', 'Technology'),
    ('celebrity', 'Celebrities'),
    ('computers', 'Computers'),
    ('educational', 'Educational'),
    ('travel', 'Travel'),
    ('kids', 'Kids'),
    ('gaming', 'Gaming'),
    ('diy', 'Diy'),
)

visibility = (
    ('public', 'Public'),
    ('private', 'Private'),
)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    page_title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ChoiceField(choices=categories)
    visibility = forms.ChoiceField(choices=visibility)
    status = forms.ChoiceField(choices=status)

    l1 = forms.CharField(max_length=150, required=False)
    ext_link1 = forms.CharField(max_length=100, required=False)

    l2 = forms.CharField(max_length=150, required=False)
    ext_link2 = forms.CharField(max_length=100, required=False)

    l3 = forms.CharField(max_length=150, required=False)
    ext_link3 = forms.CharField(max_length=100, required=False)

    l4 = forms.CharField(max_length=150, required=False)
    ext_link4 = forms.CharField(max_length=100, required=False)

    l5 = forms.CharField(max_length=150, required=False)
    ext_link5 = forms.CharField(max_length=100, required=False)


    def clean_title(self):
        title = self.cleaned_data.get("title")
        
        return title
    

    def clean_page_title(self):
        page_title = self.cleaned_data.get("page_title")
        
        return page_title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        
        return content

    def clean_category(self):
        category = self.cleaned_data.get("category")
        
        return category

    def clean_visibility(self):
        visibility = self.cleaned_data.get("visibility")
        
        return visibility

    def clean_status(self):
        status = self.cleaned_data.get("status")
        
        return status

    def clean_ext_link1(self):
        ext_link1 = self.cleaned_data.get("ext_link1")
        
        return ext_link1

    def clean_ext_link2(self):
        ext_link2 = self.cleaned_data.get("ext_link2")
        
        return ext_link2

    def clean_ext_link3(self):
        ext_link3 = self.cleaned_data.get("ext_link3")
        
        return ext_link3

    def clean_ext_link4(self):
        ext_link4 = self.cleaned_data.get("ext_link4")
        
        return ext_link4

    def clean_ext_link5(self):
        ext_link5 = self.cleaned_data.get("ext_link5")
        
        return ext_link5

    def clean_l1(self):
        l1 = self.cleaned_data.get("l1")
        
        return l1

    def clean_l2(self):
        l2 = self.cleaned_data.get("l2")
        
        return l2

    def clean_l3(self):
        l3 = self.cleaned_data.get("l3")
        
        return l3

    def clean_l4(self):
        l4 = self.cleaned_data.get("l4")
        
        return l4

    def clean_l5(self):
        l5 = self.cleaned_data.get("l5")
        
        return l5 
    
    

class UpdatePostForm(forms.Form):
    title = forms.CharField(max_length=200)
    page_title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ChoiceField(choices=categories)
    visibility = forms.ChoiceField(choices=visibility)
    status = forms.ChoiceField(choices=status)

    l1 = forms.CharField(max_length=150, required=False)
    ext_link1 = forms.CharField(max_length=100, required=False)

    l2 = forms.CharField(max_length=150, required=False)
    ext_link2 = forms.CharField(max_length=100, required=False)

    l3 = forms.CharField(max_length=150, required=False)
    ext_link3 = forms.CharField(max_length=100, required=False)

    l4 = forms.CharField(max_length=150, required=False)
    ext_link4 = forms.CharField(max_length=100, required=False)

    l5 = forms.CharField(max_length=150, required=False)
    ext_link5 = forms.CharField(max_length=100, required=False)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        
        return title
    

    def clean_page_title(self):
        page_title = self.cleaned_data.get("page_title")
        
        return page_title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        
        return content

    def clean_category(self):
        category = self.cleaned_data.get("category")
        
        return category

    def clean_visibility(self):
        visibility = self.cleaned_data.get("visibility")
        
        return visibility

    def clean_status(self):
        status = self.cleaned_data.get("status")
        
        return status
    
    def clean_ext_link1(self):
        ext_link1 = self.cleaned_data.get("ext_link1")
        
        return ext_link1

    def clean_ext_link2(self):
        ext_link2 = self.cleaned_data.get("ext_link2")
        
        return ext_link2

    def clean_ext_link3(self):
        ext_link3 = self.cleaned_data.get("ext_link3")
        
        return ext_link3

    def clean_ext_link4(self):
        ext_link4 = self.cleaned_data.get("ext_link4")
        
        return ext_link4

    def clean_ext_link5(self):
        ext_link5 = self.cleaned_data.get("ext_link5")
        
        return ext_link5

    def clean_l1(self):
        l1 = self.cleaned_data.get("l1")
        
        return l1

    def clean_l2(self):
        l2 = self.cleaned_data.get("l2")
        
        return l2

    def clean_l3(self):
        l3 = self.cleaned_data.get("l3")
        
        return l3

    def clean_l4(self):
        l4 = self.cleaned_data.get("l4")
        
        return l4

    def clean_l5(self):
        l5 = self.cleaned_data.get("l5")
        
        return l5