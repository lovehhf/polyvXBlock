#coding=utf-8
#author: lovehhf
#author_email: root@ichenfei.com
#author_blog: ichenfei.com

"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment


class PolyvXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="polyv player",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")


    app_id = String(display_name="video client_id",
    default="polyv",
    scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
    help="The  client_id for your video.")

    video_id = String(display_name="video vid",
    default="0432ade4f6cea30a891e55add8bdd997_0",
    scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
    help="The vid for your video.")


    width = Integer(display_name="Video player width",
    default="560",
    scope=Scope.content,
    help="The width for your video player.")
    height = Integer(display_name="Video player height",
    default="320",
    scope=Scope.content,
    help="The height for your video player.")

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )


    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))
    
    '''
    Main functions
    '''
    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the PolyvXBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'video_id': self.video_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/polyv_view.html', context)
        frag = Fragment(html)
        #frag.add_javascript(self.load_resource('static/js/h5connect.js')) #内有中文，使用插入外部url
        #frag.add_javascript(self.load_resource("static/js/polyv.player.min.js"))
        frag.add_javascript(self.load_resource("static/js/polyv_view.js"))
        frag.initialize_js('polyvXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'app_id' : self.app_id,
            'video_id': self.video_id,
            'width': self.width,
            'height': self.height
        }
        html = self.render_template('static/html/polyv_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/polyv_edit.js"))
        frag.initialize_js('polyvXBlockInitStudio')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_polyv(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.app_id = data['app_id']
        self.video_id = data['video_id']
        self.width = data['width']
        self.height = data['height']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when polyv init'''
        return {"video_id":self.video_id,
                "app_id":self.app_id,
                "width":self.width,
                "height":self.height
                }


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("polyv demo","<polyv/>")
        ]
