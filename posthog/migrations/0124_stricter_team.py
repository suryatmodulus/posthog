# Generated by Django 3.0.6 on 2021-02-09 09:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import posthog.models.utils


def remove_orgless_teams(apps, schema_editor):
    Team = apps.get_model("posthog", "Team")
    Team.objects.filter(organization_id__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0123_organizationinvite_first_name"),
    ]

    operations = [
        migrations.RunPython(remove_orgless_teams, migrations.RunPython.noop),
        migrations.RemoveField(model_name="team", name="opt_out_capture",),
        migrations.RemoveField(model_name="team", name="users",),
        migrations.AlterField(
            model_name="team",
            name="api_token",
            field=models.CharField(
                default=posthog.models.utils.generate_random_token,
                max_length=200,
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(
                        10, "Project's API token must be at least 10 characters long!"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(
                default="Default Project",
                max_length=200,
                validators=[django.core.validators.MinLengthValidator(1, "Project must have a name!")],
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                related_query_name="team",
                to="posthog.Organization",
            ),
        ),
    ]
